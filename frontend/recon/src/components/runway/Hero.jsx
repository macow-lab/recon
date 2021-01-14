import React, { Component } from "react";

import "../../sass/mystyles.scss";

export class Hero extends Component {
  render() {
    return (
      <div>
        <section class="hero is-medium is-primary is-bold">
          <div class="hero-body">
            <div class="container">
              <h1 class="title">Manage your wealth <br/> and reach new highs</h1>
              <h2 class="subtitle">Get a complete overview over your finances, <br/> set goals and plan for a better future.</h2>
            </div>
          </div>
        </section>
      </div>
    );
  }
}

export default Hero;
