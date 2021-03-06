import React, { useState } from "react";
import { Link, BrowserRouter, Route, Switch } from "react-router-dom";

import About from "../../pages/runway/About.js";
import Contact from "../../pages/runway/Contact.jsx";
import Main from "../../pages/runway/Main.js";
import SignIn from "../auth/InForm.jsx";

import "../../sass/mystyles.scss";

export default function Navbar() {
  const [isActive, setisActive] = React.useState(false);

  return (
    <div>
      <BrowserRouter>
        <nav className="navbar" role="navigation" aria-label="main navigation">
          <div className="navbar-brand">
            <a href="/" className="navbar-item">
              <h1 class="title is-3">recon</h1>
            </a>

            <a
              onClick={() => setisActive(!isActive)}
              role="button"
              className={`navbar-burger burger ${
                isActive ? "active" : "is-active"
              }`}
              aria-label="menu"
              aria-expanded="false"
              data-target="navbarBasic"
            >
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
            </a>
          </div>
          <div
            id="navbarBasic"
            className={`navbar-menu ${isActive ? "is-active" : ""}`}
          >
            <div className="navbar-end">
              <Link to="/" className="navbar-item">
                <h1 id="icon-text">Home</h1>
              </Link>
              <Link to="/about" className="navbar-item" id="link">
                <h1 id="icon-text">About</h1>
              </Link>
              <Link to="/contact" className="navbar-item" id="link">
                <h1 id="icon-text">Contact</h1>
              </Link>
              <Link to="/auth/login" className="navbar-item" id="link">
                <button class="button is-ghost">
                  <span class="icon is-small">
                    <i class="fas fa-sign-in-alt"></i>
                  </span>
                  <span>Log in</span>
                </button>
              </Link>
              <Link to="/auth/register" className="navbar-item" id="link">
                <button class="button is-ghost">
                  <span class="icon is-small">
                    <i class="fas fa-user-plus"></i>
                  </span>
                  <span>Sign up</span>
                </button>
              </Link>
            </div>
          </div>
        </nav>
        <Switch>
        
        <Route path="/about" component={About} />
        <Route path="/contact" component={Contact} />
        <Route path="/auth/login" component={SignIn} />
        <Route exact strict path="/" component={Main} />
        </Switch>
      </BrowserRouter>
    </div>
  );
}
