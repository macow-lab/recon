import React from "react"
import logo from './logo.svg';
import './css/mystyles.css';

import Hero from "./components/runway/Hero.jsx"

function Main(props) {
  document.title = "recon"
  return (
    <div>
      <Hero/>
      <h1>Home Page</h1>
    </div>
  )
}

export default Main;