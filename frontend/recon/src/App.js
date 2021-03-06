import React from "react";
import ReactDOM from "react-dom";
import logo from "./logo.svg";
// import "./css/mystyles.css";
// import "./App.css";
import "./sass/mystyles.scss";
import MainPage from "./pages/runway/main.jsx"
import dashboard from "./pages/dashboard/dashboard.jsx"
import Sidemenu from "./pages/dashboard/dashboard.jsx"

// Import BrowserRouter, Route and Link
import { BrowserRouter, Route, Link, Switch } from "react-router-dom";

function App() {
  document.title = "recon";
  return (
    <div>
      <BrowserRouter>
      <Switch>
      <Route path="/dash/" component={dashboard} />
      <Route path="/" component={MainPage} />
      </Switch>
      </BrowserRouter>
    </div>
  );
}

function Test() {return
}

export default App;
