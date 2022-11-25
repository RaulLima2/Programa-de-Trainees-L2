import { Nav, Navbar, Container, Button, ButtonGroup, ButtonToolbar} from 'react-bootstrap';


import 'bootstrap/dist/css/bootstrap.min.css';

import logo from '../../logo.png';

function NavBarHeader() {
  return (
      <Navbar bg="dark" variant="dark" sticky='top'>
        <Container fluid>
          <Navbar.Brand href="#home"><img src={logo} className="App-logo" alt="logo" /></Navbar.Brand>
          <Navbar.Toggle aria-controls="navbarScroll" />
          <Navbar.Collapse id="navbarScroll" className='justify-content-center'>
            <Nav navbarScroll>
              <Nav.Item>
                <Nav.Link href='#auctions'>Auctions</Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link href='#roadmap'>Roadmap</Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link href='#discover'>Discover</Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link href='#community'>Community</Nav.Link>
              </Nav.Item>
            </Nav>
          </Navbar.Collapse>
          <ButtonToolbar className='Toolbar with button groups'>
            <ButtonGroup className="me-4">
                <Button variant="outline-primary">Contact</Button>
            </ButtonGroup>
            <ButtonGroup className="me-4" aria-label="Second group">
                <Button variant="primary">My account</Button>
            </ButtonGroup>
          </ButtonToolbar>
        </Container>
      </Navbar>
  );
}

export default NavBarHeader;
