
import { SidebarMenu, SidebarMenuButton, SidebarMenuItem } from './ui/sidebar'
import { Brain } from 'lucide-react'

const NavHeader = () => {
  return (
    <SidebarMenu>
      <SidebarMenuItem>
        <SidebarMenuButton >
          <Brain/>
          <a href="#" className='text-base font-semibold'>Gyrus Inc.</a>
        </SidebarMenuButton>
      </SidebarMenuItem>
    </SidebarMenu>
  )
}

export default NavHeader