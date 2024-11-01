import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
//importamos las páginas
import { Home } from "./pages/Home";
import { Register } from "./pages/Register";
import  { Navbar }   from "./components/Navbar";

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Navigate to="/home" />} />
        <Route path="/home" element={<Home />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
