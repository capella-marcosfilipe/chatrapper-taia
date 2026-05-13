import { Message } from '@/types';

export default function MessageBubble({ message }: { message: Message }) {
  const isUser = message.role === 'user';

  return (
    <div className={`result-card message-card ${isUser ? 'user-message' : 'assistant-message'}`}>
      <div className="result-top">
        <div>
          <div className="result-title">{isUser ? 'VOCÊ' : 'CANÃO'}</div>
        </div>
        {!isUser && (
          <a 
            className="result-link" 
            href="#" 
            onClick={(e) => e.preventDefault()}
          >
            // RAG + LangGraph ↗
          </a>
        )}
      </div>
      <div className="result-text">{message.content}</div>
    </div>
  );
}