import React from "react";
import ReactDOM from "react-dom";
import logo from "./logo.svg";
// import "./css/mystyles.css";
// import "./App.css";
import "./sass/mystyles.scss";
import MainPage from "./pages/runway/main.jsx"

// Import BrowserRouter, Route and Link
import { BrowserRouter, Route, Link } from "react-router-dom";

function App() {
  document.title = "recon";
  return (
    <div>
      <MainPage></MainPage>
    </div>
  );
}

function Test() {return
}

export default App;
