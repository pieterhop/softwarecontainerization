import React, { useState, useRef, useEffect } from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Apps from './Apps';
import axios from 'axios'

const apiPort = '30007'
const apiURL = 'http://localhost'

 //const [getMessage, setGetMessage] = useState({})



// componentDidMount() {
//   axios.get(apiURL+':'+apiPort+'/todos',{ crossDomain: true }).then(response => {
//     console.log("SUCCESS", response)
//     setGetMessage(response)
//   }).catch(error => {
//     console.log(error)
//   })
// }

const DATA = [
  {
      "complete": false,
      "id": 1,
      "title": "test"
  },
  {
      "complete": false,
      "id": 2,
      "title": "test"
  },
  {
      "complete": false,
      "id": 3,
      "title": "test"
  }
];

ReactDOM.render(
  <React.StrictMode>
    <Apps />
  </React.StrictMode>,
  document.getElementById('root')
);
