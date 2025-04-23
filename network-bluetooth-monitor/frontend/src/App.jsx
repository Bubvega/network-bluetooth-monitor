import React, { useEffect, useState } from 'react';
import DeviceList from './components/DeviceList';

function App() {
  const [devices, setDevices] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/devices")
      .then(res => res.json())
      .then(data => setDevices(data));
  }, []);

  return (
    <div className="App">
      <h1>Network & Bluetooth Monitor</h1>
      <DeviceList devices={devices} />
    </div>
  );
}

export default App;