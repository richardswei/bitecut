import React from 'react';
import './LoginForm.css'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

const LoginForm = () =>
<Form className='LoginForm'>
  <Form.Group controlId="formBasicEmail">
    <Form.Label className='LoginForm-label'>Email address</Form.Label>
  <Form.Control type="email" placeholder="Enter email" className="LoginForm-textline" />
  </Form.Group>

  <Form.Group controlId="formBasicPassword">
    <Form.Label className='LoginForm-label'>Password</Form.Label>
  <Form.Control type="password" placeholder="Password" className='LoginForm-textline' />
  </Form.Group>
  <Button variant="primary" type="submit" className='LoginForm-submit'>
    Submit
  </Button>
</Form>

export default LoginForm
