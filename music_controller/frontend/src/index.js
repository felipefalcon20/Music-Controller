import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './components/App';

// Create a root.
const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);

// Initial render: Render an element to the root.
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
