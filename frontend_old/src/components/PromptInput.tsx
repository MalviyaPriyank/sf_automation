import { ArrowUpIcon, Plus } from "lucide-react"
import { InputGroup, InputGroupAddon, InputGroupButton, InputGroupInput, InputGroupText, InputGroupTextarea } from "./ui/input-group"
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "./ui/dropdown-menu"
import { Separator } from "./ui/separator"
import { forwardRef } from "react"

type PromptInputProps = {
    message: string
    onMessageChange: (value: string) => void
    onSend: () => void
    disabled?: boolean
}


const PromptInput = forwardRef<HTMLTextAreaElement, PromptInputProps>(({ message, onMessageChange, onSend, disabled }, ref) => {
    const handleChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
        const value = e.target.value
        console.log(value)
        onMessageChange(value)
    }

    return (
        <InputGroup>
            <InputGroupTextarea
                ref={ref}
                placeholder="Ask Frosty"
                onChange={handleChange}
                value={message}
                onKeyDown={(e) => {
                    if (e.key === "Enter" && !e.shiftKey) {
                        e.preventDefault()
                        onSend()
                    }
                }}
            />
            <InputGroupAddon align="block-end">
                <InputGroupButton
                    variant="outline"
                    className="rounded-full"
                    size="icon-xs"
                >
                    <Plus />
                </InputGroupButton>
                <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                        <InputGroupButton variant="ghost">Auto</InputGroupButton>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent
                        side="top"
                        align="start"
                        className="[--radius:0.95rem]"
                    >
                        <DropdownMenuItem>Auto</DropdownMenuItem>
                        <DropdownMenuItem>Agent</DropdownMenuItem>
                        <DropdownMenuItem>Manual</DropdownMenuItem>
                    </DropdownMenuContent>
                </DropdownMenu>
                <InputGroupText className="ml-auto"></InputGroupText>
                <InputGroupButton
                    variant='default'
                    className="rounded-full"
                    size='icon-xs'
                    disabled={disabled}
                    onClick={onSend}>
                    <ArrowUpIcon />
                    <span className="sr-only">Send</span>
                </InputGroupButton>
            </InputGroupAddon>
        </InputGroup>
    )
})

export default PromptInput