import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import Projects from './components/Projects';
import Contact from './components/Contact';

function App() {
  return (
    <div className="App">
      <Header />
      <Projects />
      <Contact />
      <Footer />
    </div>
  );
}

export default App;
