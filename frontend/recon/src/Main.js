import React from "react"
import logo from './logo.svg';
import './css/mystyles.css';

import Hero from "./components/runway/Hero.jsx"

function Main(props) {
  document.title = "recon"
  return (
    <div>
      <Hero></Hero>
      <h1>Projects</h1>
    </div>
  )
}
 
export default Main;