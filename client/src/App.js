
import React, {Component} from 'react';
import { Form, Container } from 'react-bootstrap';
import { instanceOf } from 'prop-types'
import { withCookies, Cookies } from 'react-cookie'

import { HashRouter as Router, Switch, Route, } from "react-router-dom";
import { Redirect } from "react-router-dom";
import Navigation from "./Navigation.js";
import MapPage from "./MapPage.js";
import NotFound from "./NotFound.js";
import './App.css';


function App() {
  return (
    <Router>
        <Navigation />
        <Container>
        <Switch>
         <Route exact path="/" 
           render={
             (routeProps) =>
               <MapPage /*{...routeProps} appState={this.state}*//> 
           } 
         />
         <Route component={NotFound} />

        </Switch>
      </Container>
    </Router>

  );
}

export default App;
