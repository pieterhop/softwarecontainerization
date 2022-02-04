import React, { useState, useRef, useEffect } from "react";
import Form from "./components/Form";
import FilterButton from "./components/FilterButton";
import Todo from "./components/Todo";
import { nanoid } from "nanoid";
import axios from 'axios'
import App from './App';

const apiPort = '30007'
const apiURL = 'http://34.77.230.60'

var res=[]
var res2

function Apps() {
  const [getMessage, setGetMessage] = useState({})
  const [isLoading, setLoading] = useState(true)
useEffect(()=>{
  axios.get(apiURL+':'+apiPort+'/todos',{ crossDomain: true }).then(response => {
    res = response.data
    //resArray = JSON.stringify(res)
    console.log("SUCCESS A2", res)
    setGetMessage(response)
    setLoading(false)
  }).catch(error => {
    console.log(error)
  })
 
}, [])

if (isLoading){
  return <div className="App">Loading...</div>;
}

return(
<App tasks={res} />
)
}

export default Apps;
