import { DropdownMenu, DropdownMenuContent, DropdownMenuTrigger, DropdownMenuItem, DropdownMenuSeparator } from "./ui/dropdown-menu"
import { SidebarMenu, SidebarMenuButton, SidebarMenuItem, useSidebar } from "./ui/sidebar"
import { Avatar, AvatarFallback, AvatarImage } from "./ui/avatar"
import { EllipsisVertical, LogOut, LogOutIcon, ReceiptText, Settings } from "lucide-react"
import { useState } from "react"
import SettingsDialog from "./SettingsDialog"

type User = {
  name: string
  email: string
  avatar: string
}
type NavUserProps = {
  user: User
}


const NavUser = ({ user: { name, email, avatar } }: NavUserProps) => {
  const { isMobile } = useSidebar()
  const [settingsOpen, setSettingsOpen] = useState(false)

  return (
    <>
      <SidebarMenu>
        <SidebarMenuItem>
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <SidebarMenuButton
                size="lg">
                <Avatar>
                  <AvatarImage src="https://github.com/shadcn.png" alt="@name" />
                  <AvatarFallback>CN</AvatarFallback>
                </Avatar>
                <div className="flex flex-col">
                  <span>{name}</span>
                  <span className="text-muted-foreground text-xs">{email}</span>
                </div>
                <EllipsisVertical className="ml-auto" />
              </SidebarMenuButton>
            </DropdownMenuTrigger>

            <DropdownMenuContent
              side={isMobile ? "bottom" : "right"}
              className="w-[--radix-popper-anchor-width]"
            >
              <DropdownMenuItem onClick={() => setSettingsOpen(true)}>
                <Settings />
                <span>Settings</span>
              </DropdownMenuItem>

              <DropdownMenuItem onClick={() => setSettingsOpen(true)}>
                <ReceiptText />
                <span>Billing</span>
              </DropdownMenuItem>

              <DropdownMenuSeparator />

              <DropdownMenuItem>
                <LogOut />
                <span>Sign out</span>
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </SidebarMenuItem>
      </SidebarMenu>

      <SettingsDialog open={settingsOpen} onOpenChange={setSettingsOpen}>

      </SettingsDialog>
    </>
  )
}

export default NavUser