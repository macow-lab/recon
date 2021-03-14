import React, { useState, Component } from "react";
import { Link, BrowserRouter, Route } from "react-router-dom";
import "../../sass/mystyles.scss";

export default function Sidemenu() {
  return (
    <div>
      <aside class="menu">
        <p class="menu-label">General</p>
        <ul class="menu-list">
          <li>
            <a href="/dash/">
              <span class="icon is-small">
                <i class="fas fa-home"></i>
                Home
              </span>
            </a>
          </li>
          <li>
            <a href="/dash/budget">
            <span class="icon is-small">
                <i class="fas fa-chart-pie"></i>
                Budget
              </span>
            </a>
          </li>
          <li>
            <a href="/dash/networth">
            <span class="icon is-small">
                <i class="fas fa-chart-line"></i>
                Networth
              </span>
            </a>
          </li>
        </ul>
        <p class="menu-label">Settings</p>
        <ul class="menu-list">
          <li>
            <a href="/dash/settings">Change Settings</a>
          </li>
        </ul>
      </aside>
    </div>
  );
}
