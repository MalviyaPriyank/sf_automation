import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuTrigger,
  DropdownMenuItem,
  DropdownMenuSeparator,
} from "./ui/dropdown-menu";
import {
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  useSidebar,
} from "./ui/sidebar";
import { Avatar, AvatarFallback, AvatarImage } from "./ui/avatar";
import {
  EllipsisVertical,
  LogOut,
  ReceiptText,
  Settings,
} from "lucide-react";
import { useState } from "react";
import SettingsDialog from "./SettingsDialog";
import useUser from "@/hooks/useUser";
import { Skeleton } from "./ui/skeleton";
import { logout } from "@/lib/api";
import queryClient from "@/config/queryClient";

const NavUser = () => {
  const { isMobile } = useSidebar();
  const [settingsOpen, setSettingsOpen] = useState(false);
  const { user } = useUser();

  const displayName = user?.name?.trim() || <Skeleton className="h-4 w-[100px] mb-1" />;
  const displayEmail = user?.email?.trim() || <Skeleton className="h-4 w-[150px] mt-1" />;
  const nameOrEmail = (user?.name || user?.email || "").trim();
  const initials = nameOrEmail
    ? nameOrEmail
        .split(/\s+/)
        .slice(0, 2)
        .map((part) => part[0]?.toUpperCase())
        .join("")
    : "U";
  const displayPicture = user?.picture;

  const handleLogout = async () => {
    await logout();
    localStorage.removeItem("user_id");
    queryClient.clear();
    window.location.reload();
  }


  return (
    <>
      <SidebarMenu>
        <SidebarMenuItem>
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <SidebarMenuButton size="lg">
                <Avatar>
                  <AvatarImage
                    src={displayPicture || "https://github.com/shadcn.png"}
                    alt="@name"
                  />
                  <AvatarFallback>{initials}</AvatarFallback>
                </Avatar>
                <div className="flex flex-col">
                  <span>{displayName}</span>
                  <span className="text-muted-foreground text-xs">{displayEmail}</span>
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

              <DropdownMenuItem onClick={() => handleLogout()}>
                <LogOut />
                <span>Sign out</span>
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </SidebarMenuItem>
      </SidebarMenu>

      <SettingsDialog
        open={settingsOpen}
        onOpenChange={setSettingsOpen}
      ></SettingsDialog>
    </>
  );
};

export default NavUser;
