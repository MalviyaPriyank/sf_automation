import { useState, useRef, useEffect } from "react"
import axios from "axios"

import { useSidebar } from "./ui/sidebar"
import PromptInput from "./PromptInput"
import Message from "./Message"

type MessageType = {
  role: "user" | "assistant"
  content: string
}

const Chat = () => {
  const { state, isMobile } = useSidebar()

  const [message, setMessage] = useState("")
  const [messages, setMessages] = useState<MessageType[]>([])

  const inputRef = useRef<HTMLTextAreaElement>(null)
  const bottomRef = useRef<HTMLDivElement | null>(null)

  const getLeftPadding = () => {
    if (isMobile) return "1rem"
    return state === "expanded" ? "calc(var(--sidebar-width) + 1rem)" : "1rem"
  }

  const handleSend = async () => {
    if (!message.trim()) return

    const userMessage: MessageType = { role: "user", content: message }

    // Add user message immediately
    setMessages(prev => [...prev, userMessage])
    setMessage("")

    try {
      const res = await axios.post("http://localhost:80/echo", { message })
      const assistantMessage: MessageType = {
        role: "assistant",
        content: res.data.reply,
      }

      setMessages(prev => [...prev, assistantMessage])
    } catch (error) {
      console.error("Error sending message:", error)
    }
  }

  // Auto-focus textarea when user starts typing and nothing is focused
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (
        e.key.length === 1 &&
        !e.ctrlKey &&
        !e.metaKey &&
        !e.altKey
      ) {
        const activeElement = document.activeElement
        if (
          activeElement?.tagName !== "INPUT" &&
          activeElement?.tagName !== "TEXTAREA"
        ) {
          inputRef.current?.focus()
        }
      }
    }

    window.addEventListener("keydown", handleKeyDown)
    return () => window.removeEventListener("keydown", handleKeyDown)
  }, [])

  // Smooth scroll to bottom whenever messages change
  useEffect(() => {
    if (bottomRef.current) {
      bottomRef.current.scrollIntoView({ behavior: "smooth" })
    }
  }, [messages])

  return (
    <>
      <div className="flex-1 overflow-y-auto pb-32">
        {messages.map((msg, index) => (
          <Message key={index} role={msg.role} content={msg.content} />
        ))}

        {/* Dummy div to scroll into view */}
        <div ref={bottomRef} />
      </div>

      <div
        className="fixed bottom-0 left-0 right-0 p-4 transition-all duration-200 ease-linear"
        style={{ paddingLeft: getLeftPadding() }}
      >
        <div className="max-w-4xl mx-auto bg-background rounded-lg">
          <PromptInput
            ref={inputRef}
            message={message}
            onMessageChange={setMessage}
            onSend={handleSend}
            disabled={!message.trim()}
          />
        </div>
      </div>
    </>
  )
}

export default Chat
