import React, { Component } from "react";

import "../../sass/mystyles.scss";

export class Hero extends Component {
  render() {
    return (
      <div>
        <section class="hero is-fullheight-with-navbar has-bg-img">
          <div class="hero-body">
            <div class="container">
              <h1 class="title">Manage your wealth <br/> and reach new highs</h1>
              <h2 class="subtitle">Get a complete overview over your finances, <br/> set goals and plan for a better future.</h2>
              <button class="button is-info">GET STARTED</button>
            </div>
          </div>
        </section>
      </div>
    );
  }
}

export default Hero;
