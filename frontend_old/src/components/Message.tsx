import { cn } from "@/lib/utils"
import { Button } from "./ui/button"
import { Tooltip, TooltipContent, TooltipTrigger } from "./ui/tooltip"
import { Check, Copy, Flag, ThumbsDown, ThumbsUp } from "lucide-react"
import { useEffect, useRef, useState } from "react"

type MessageProps = {
  content: string
  role: "user" | "assistant"
}

const Message = ({ content, role }: MessageProps) => {
  const isUser = role === "user"
  const [copyClicked, setCopyClicked] = useState(false)
  const timeoutRef = useRef<number | null>(null)

  async function handleCopy() {
    await navigator.clipboard.writeText(content)
    setCopyClicked(true)

    // clear any previous timer so they don't stack
    if (timeoutRef.current) {
      window.clearTimeout(timeoutRef.current)
    }

    timeoutRef.current = window.setTimeout(() => {
      setCopyClicked(false)
    }, 5000)
  }

  // optional: cleanup on unmount
  useEffect(() => {
    return () => {
      if (timeoutRef.current) {
        window.clearTimeout(timeoutRef.current)
      }
    }
  }, [])

  return (
    <div className="max-w-4xl mx-auto">
      <div className={cn("flex w-full py-8",
        isUser ? "justify-end" : "justify-start"
      )}>
        <div className="flex flex-col max-w-[75%] gap-2">
          <div className={cn("whitespace-pre-wrap inline-flex",
            isUser ? "bg-blue-500 p-2 rounded-xl self-end" : "self-start"
          )}>
            {content}
          </div>
          <span className={cn(isUser ? "self-end" : "self-start")}>
            <Tooltip>
              <TooltipTrigger>
                <Button variant="ghost" size="icon-sm" onClick={handleCopy}>
                  {copyClicked ? <Check /> : <Copy />}
                </Button>
              </TooltipTrigger>
              <TooltipContent side="bottom">
                Copy
              </TooltipContent>
            </Tooltip>
            {!isUser &&
              <>
                <Tooltip>
                  <TooltipTrigger>
                    <Button variant="ghost" size="icon-sm" onClick={handleCopy}>
                      <ThumbsUp />
                    </Button>
                  </TooltipTrigger>
                  <TooltipContent side="bottom">
                    Good response
                  </TooltipContent>
                </Tooltip>
                <Tooltip>
                  <TooltipTrigger>
                    <Button variant="ghost" size="icon-sm" onClick={handleCopy}>
                      <ThumbsDown />
                    </Button>
                  </TooltipTrigger>
                  <TooltipContent side="bottom">
                    Bad response
                  </TooltipContent>
                </Tooltip>
                <Tooltip>
                  <TooltipTrigger>
                    <Button variant="ghost" size="icon-sm" onClick={handleCopy}>
                      <Flag />
                    </Button>
                  </TooltipTrigger>
                  <TooltipContent side="bottom">
                    Report message
                  </TooltipContent>
                </Tooltip>
              </>
            }
          </span>
        </div>
      </div>
    </div>
  )
}

export default Message