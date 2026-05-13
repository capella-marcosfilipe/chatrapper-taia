import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Sabotage Similarity • Chatbot",
  description: "Chatbot RAG com letras do Sabotage - TAIA AV02",
  icons: {
    icon: "/favicon.ico",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR">
      <body>
        {children}
      </body>
    </html>
  );
}