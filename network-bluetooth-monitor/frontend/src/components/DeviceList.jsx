import React from 'react';

const DeviceList = ({ devices }) => (
  <div>
    <h2>Dispositivi rilevati:</h2>
    <ul>
      {devices.map((dev, index) => (
        <li key={index}>
          IP: {dev.ip || "—"} - MAC: {dev.mac || "—"} - Tipo: {dev.type}
        </li>
      ))}
    </ul>
  </div>
);

export default DeviceList;