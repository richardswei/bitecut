import React, {Component} from 'react'
// import { Link, withRouter  } from "react-router-dom";
import {Container,
  ListGroup
} from 'react-bootstrap'
import data from "./places.json";
import tt from '@tomtom-international/web-sdk-maps';
function getApiResponse(dbPath) {
  let places = data;
  return places;
}

function getCoordinates(response) {
}

function buildMap() {
  const productInfo = tt.setProductInfo('BiteCut', 'v0.1');
  const map = tt.map({
    key: "YWKYyuclIju4nZDJKYoXXgkuLECnJrsx",
    container: 'map',
    center: [4.573040, 52.138950],
    style: 'tomtom://vector/1/basic-main',
    zoom: 9
  });
}


class MapPage extends Component {
  componentDidMount() {
    buildMap()
  }
  render() { 
    return (
      <div>
        <Container>
          <div className='map' id='map'></div>
          <ListGroup>
            {
              getApiResponse("./places.json").map((place) => {
                return (<ListGroup.Item key={place.position.lat + place.position.lon}>
                  <strong>{place.name}</strong>
                </ListGroup.Item>)
              })
            }
          </ListGroup>
        </Container>  
      </div>
    )
  }
}

export default MapPage

