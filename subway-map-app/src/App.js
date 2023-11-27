import { useEffect, useState } from 'react';
import { ReactComponent as SubwayMap } from './map.svg';
import './App.css';

function App() {
  const [isMenuVisible, setMenuVisibility] = useState(false);
  const [menuMessage, setMenuMessage] = useState('');

  const handleStationClick = (station) => {
    console.log('Station clicked:', station);
    setMenuMessage(`Station was clicked: ${station.getAttribute('class')}`);
    setMenuVisibility(true);
  };

  useEffect(() => {
    // Delay execution to ensure SVG is fully loaded
    setTimeout(() => {
      const stations = document.querySelectorAll('.st25, .st45');

      stations.forEach(station => {
        station.addEventListener('click', () => handleStationClick(station));
      });

      // Clean up event listeners
      return () => {
        stations.forEach(station => {
          station.removeEventListener('click', () => handleStationClick(station));
        });
      };
    }, 500); // Delay of 500ms; adjust as needed
  }, []);


  return (
    <div className="App">
      <header className="App-header">
        <SubwayMap className="Subway-map" />

        {isMenuVisible && (
          <div className="Menu">
            {menuMessage}
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
