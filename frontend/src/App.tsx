
import Layout from "./components/Layout"
import Chat from "./components/Chat"
import { ThemeProvider } from "./components/ThemeProvider"

function App() {

  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <Layout>
        <Chat/>
      </Layout>
    </ThemeProvider>
  )
}

export default App
