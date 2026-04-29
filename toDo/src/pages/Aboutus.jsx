// AboutUs.jsx
import React from "react";


const Aboutus = () => {
  return (
    <section className="aboutus">
      <div className="aboutus-container">
        <h1 className="aboutus-title">About Us</h1>
        <p className="aboutus-subtitle">
          We are passionate about building modern digital solutions that help businesses grow.
        </p>

        <div className="aboutus-cards">
          <div className="aboutus-card">
            <h2>Who We Are</h2>
            <p>
              A creative team of developers, designers, and thinkers delivering quality products.
            </p>
          </div>

          <div className="aboutus-card">
            <h2>Our Mission</h2>
            <p>
              To provide innovative, affordable, and scalable solutions for every client.
            </p>
          </div>

          <div className="aboutus-card">
            <h2>Why Choose Us</h2>
            <p>
              We focus on trust, transparency, and customer satisfaction.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Aboutus;