import { Box, Container, Toolbar } from "@mui/material";
import Dashboard from "./pages/Dashboard";
import Well from "./pages/Well"
import Comunication from "./pages/Comunication"
import NavBar from "./components/layout/NavBar";

import { Route, Routes } from "react-router-dom";

export default function App() {
  return (
    <Box sx={{ display: "flex" }}>
      <NavBar />
      <Container maxWidth="xl" sx={{ mt: 2 }}>
        <Toolbar />
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/well" element={<Well />} />
          <Route path="/comm" element={<Comunication />} />
        </Routes>         

      </Container>
    </Box>
  );
}
