/*
class Listing(db.Model):
    __tablename__ = 'listing'
    listing_ID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    provider_email = db.Column(db.String(64), db.ForeignKey('provider.email'), nullable = False)
    dish = db.Column(db.String(64))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    type = db.Column(db.String(64))
 */
 import React from 'react';
 import './NewListingForm.css'
 import Form from 'react-bootstrap/Form'
 import Button from 'react-bootstrap/Button'
 import Image from 'react-bootstrap/Image'

class NewListingForm extends React.Component {
  defaultState = {
    previewImage: './foods.svg'
  }
  initialState = {
    hasPrice: false,
    hasDiscount: false,
  }
  constructor(props) {
    super(props)
    this.updatePreview = this.updatePreview.bind(this)
    this.updateOriginalPrice = this.updateOriginalPrice.bind(this)
    this.updatePercent = this.updatePercent.bind(this)
    this.conditionallyShowPrice = this.conditionallyShowPrice.bind(this)
    this.state = {...this.initialState, ...this.defaultState}
  }
  updatePreview(event) {
    if (event.target.files && event.target.files[0]){
      const file = event.target.files[0]
      const reader = new FileReader
      reader.addEventListener('load', event => this.setState({previewImage: event.target.result}))
      reader.readAsDataURL(file)
    }
  }
  updateOriginalPrice(event) {
    if (event.target.value) {
      const numValue = Number.parseFloat(event.target.value)
      this.setState({hasPrice: true, original: numValue})
      this.updatePriceDisplay(numValue, this.state.discount)
    } else {
      this.setState({hasPrice: false})
    }
  }
  updatePercent(event) {
    if (event.target.value) {
      const numValue = Number.parseInt(event.target.value, 10)


      this.setState({hasDiscount: true, discount: numValue})
      this.updatePriceDisplay(this.state.original, numValue)
    } else {
      this.setState({hasDiscount: false})
    }
  }
  updatePriceDisplay(price, discount) {
    this.setState({finalPrice: (price-price*discount/100).toFixed(2)})
  }
  conditionallyShowPrice(price, discount) {
    return this.state.hasDiscount && this.state.hasPrice && <div className="NewListingForm-label">Price after discount: {this.state.finalPrice}</div>
  }
  render() {
    return (
      <Form className='NewListingForm' onSubmit={(event) => event.preventDefault()||this.props.onSubmit&&this.props.onSubmit()}>
        <Form.Group controlId="formImage">
          <Form.Label className="NewListingForm-label">
            Image
            <Image src={this.state.previewImage} className="NewListingForm-image" />
          </Form.Label>
          <Form.Control type="file" className="NewListingForm-imageForm" placeholder="Upload photo" accept='image/*' onChange={this.updatePreview}/>
        </Form.Group>
        <Form.Group controlId="formDescription">
          <Form.Label className='NewListingForm-label'>Description</Form.Label>
          <Form.Control type="email" placeholder="Enter description" className="NewListingForm-textline" />
        </Form.Group>

        <Form.Group controlId="formPrice">
          <Form.Label className='NewListingForm-label'>Price</Form.Label>
        <Form.Control type="number" placeholder="0.00" min="0" step="0.01" className='NewListingForm-money' onChange={this.updateOriginalPrice}/>
        </Form.Group>
        <Form.Group controlId="formDiscount">
          <Form.Label className='NewListingForm-label' onChange={this.updatePercent}>Discount</Form.Label>
        <Form.Control type="number" placeholder="0" min="0" max="100" className="NewListingForm-percent" onChange={this.updatePercent} /><span className='NewListingForm-percent-sign'>%</span>
        </Form.Group>
        {this.conditionallyShowPrice()}
        <Button variant="primary" type="submit" className='LoginForm-submit'>
          Save
        </Button>
      </Form>
    )
  }
}

 export default NewListingForm
