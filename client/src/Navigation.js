import React, {Component} from 'react'
import {Container, Navbar, Nav, NavDropdown} from 'react-bootstrap'
import { Link, withRouter  } from "react-router-dom";

class Navigation extends Component {

  render() { 
    return  <div>
    <Navbar expand="lg" bg="primary" variant="dark">     
      <Container>

      <Navbar.Brand as={Link} to="/">
        <h1 className='brand'>BiteCut</h1>
      </Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav>
            <Nav.Link as={Link} to="/NewEntry">New Entry</Nav.Link>
            <NavDropdown alignRight title={"Account"} id="collasible-nav-dropdown">
                <div>
                  <NavDropdown.Item as={Link} to="/sign-in">Log In</NavDropdown.Item>
                  <NavDropdown.Item as={Link} to="/Signup">Sign Up</NavDropdown.Item>
                </div>
                <div>
                  <NavDropdown.Header>Signed in as:
                    <strong>BIGBOY</strong>
                  </NavDropdown.Header>
                  <NavDropdown.Divider />
                  <NavDropdown.Item as={Link} to="/sign-out">Sign Out</NavDropdown.Item>
                </div>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>

      </Container>      
    </Navbar>
    </div>
  }
}

export default withRouter(Navigation)