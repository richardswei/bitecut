import React, {Component} from 'react'
// import { Link, withRouter  } from "react-router-dom";
import {Container,
  ListGroup,
  Row,
  Col
} from 'react-bootstrap'
import data from "./places.json";
import tt from '@tomtom-international/web-sdk-maps';
function getApiResponse(dbPath) {
  let places = data;
  return places;
}

// function getCoordinatesFromTT(response) {
// }

const getLocation = () => new Promise(
  (resolve, reject) => {
    navigator.geolocation.getCurrentPosition(
      position => {
        const location = {
          lat:position.coords.latitude,
          long:position.coords.longitude
        };
        console.log(location)
        resolve(location); // Resolve with location. location can now be accessed in the .then method.
      },
      err => reject(err) // Reject with err. err can now be accessed in the .catch method.
    );
  }
);

/**
 * then is called when the Promise is resolved
 * catch is called when the Promise rejects or encounters an error.
 */
getLocation()
    .then(location => console.log(location))
    .catch(error => console.log(error));

function buildMap(coords) {
  const productInfo = tt.setProductInfo('BiteCut', 'v0.1');
  const map = tt.map({
    key: "YWKYyuclIju4nZDJKYoXXgkuLECnJrsx",
    container: 'map',
    center: isNaN(coords.lat) || isNaN(coords.lon) ? [-122.40100, 37.78803] : [coords.lat, coords.lon],
    style: 'tomtom://vector/1/basic-main',
    zoom: 15
  });
}


class MapPage extends Component {
  componentDidMount() {
    buildMap(getLocation)
  }
  render() { 
    return (
      <div>
        <Container>
          <Row> 
            <div className='map' id='map'></div>
          </Row>
        </Container>
        <Container>

          <ListGroup>
            {
              getApiResponse("./places.json").map((place,i) => {
                return (<ListGroup.Item key={i}>
                  <strong>{place.name}</strong>
                  <div>{place.address}</div>
                  <div>{place.email}</div>
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

