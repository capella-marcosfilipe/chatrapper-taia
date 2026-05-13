'use client';

import { useState, useRef, useEffect } from 'react';
import ChatHeader from '@/components/ChatHeader';
import MessageBubble from '@/components/MessageBubble';
import LoadingDots from '@/components/LoadingDots';
import { Message } from '@/types';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: 'assistant',
      content: 'E aí, quebrada! Sou o Canão no modo RAG + LangGraph. Pode mandar sua pergunta que eu recupero os trechos das minhas letras e te respondo com o flow original.'
    }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || loading) return;

    const userMsg: Message = { role: 'user', content: input.trim() };
    setMessages((prev) => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    try {
      const res = await fetch(`${API_URL}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mensagem: userMsg.content, historico: messages }),
      });

      if (!res.ok) throw new Error(`Erro na API: ${res.status}`);

      const data = await res.json();
      const botMsg: Message = { role: 'assistant', content: data.resposta };
      setMessages((prev) => [...prev, botMsg]);
    } catch {
      const errMsg: Message = {
        role: 'assistant',
        content: 'Erro ao processar a pergunta. Verifica se o back tá de pé, mano.'
      };
      setMessages((prev) => [...prev, errMsg]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <ChatHeader />

      <div className="results-header">// conversa com o canão — RAG + LangGraph</div>

      <div className="results chat-container">
        {messages.map((msg, index) => (
          <MessageBubble key={index} message={msg} />
        ))}
        {loading && <LoadingDots />}
        <div ref={chatEndRef} />
      </div>

      <form className="input-section" onSubmit={handleSubmit}>
        <label className="field-label">// sua pergunta</label>
        <textarea
          className="textarea"
          placeholder="escreve aí sua pergunta pro Canão..."
          rows={3}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          disabled={loading}
        />
        <button className="btn-analyze" type="submit" disabled={loading || !input.trim()}>
          {loading ? 'PROCESSANDO...' : '▶ PERGUNTAR AO CANÃO'}
        </button>
      </form>

      <footer className="footer">
        <span>// embeddings via sentence-transformers</span>
        <span>CANÃO, ZL</span>
      </footer>
    </div>
  );
}