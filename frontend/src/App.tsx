import { Route, Routes } from "react-router-dom";
import Layout from "./components/Layout";
import Chat from "./components/Chat";
import { ThemeProvider } from "./components/ThemeProvider";
import PrivacyPolicy from "./pages/PrivacyPolicy";
import TermsOfUse from "./pages/TermsOfUse";

function App() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <Routes>
        <Route
          path="/"
          element={
            <Layout>
              <Chat />
            </Layout>
          }
        />
        <Route path="/policies/privacy-policy/" element={<PrivacyPolicy />} />
        <Route path="/policies/terms-of-use/" element={<TermsOfUse />} />
      </Routes>
    </ThemeProvider>
  );
}

export default App;
