import React from 'react';
import { Container, Row, Col, Button, Form, InputGroup } from 'react-bootstrap';

import logo from './logo.png';

function Footer() {
    return (
        <footer className='App-footer'>
            <Container fluid>
                <Row>
                    <Col >
                        <img src={logo} className="App-logo" alt="logo" />
                        Support
                        Terms of Service
                        License
                    </Col>
                    <Col>
                        <h4>Auctions</h4>
                        <h4>Roadmap</h4>
                        <h4>Discover</h4>
                        <h4>Community</h4>
                    </Col>
                    <Col>
                        <InputGroup className="mb-3">
                            <Form.Control
                                placeholder="Newsletter"
                                aria-label="Newsletter"
                                aria-describedby="basic-addon2"
                            />
                            <Button variant="line-secondary" id="button-addon2">
                                Sign in
                            </Button>
                        </InputGroup>
                    </Col>
                </Row>
            </Container>
        </footer>
    );
}

export default Footer;