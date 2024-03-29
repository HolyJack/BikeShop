const HomePage = () => {
  return (
    <div className=" mx-auto my-2 w-2/4 h-full flex flex-col justify-center font-mono text-center">
      <h1 className=" mt-2 text-2xl font-bold">Welcome to our Bike Shop!</h1>
      <h1 className=" mb-2 text-2xl font-bold">
        Your One-Stop Destination for Cycling Enthusiasts!
      </h1>
      <p className=" my-2">
        At BikeShop.com, we are passionate about two things - bikes and
        providing an exceptional shopping experience for all cycling enthusiasts
        out there. Whether you're a seasoned rider, a weekend warrior, or just
        discovering the joy of biking, we've got everything you need to elevate
        your cycling journey.
      </p>
      <p className=" my-2">
        Our motto is simple -{" "}
        <span className=" font-bold text-yellow-400">
          "Ride with Passion, Shop with Confidence."
        </span>{" "}
        We believe that biking is not just a sport or a mode of transportation;
        it's a way of life, a form of freedom, and a source of endless
        adventure. That's why we strive to be more than just an ordinary
        ecommerce shop. We aim to be your trusted companion, offering top-notch
        products and outstanding service that will make your biking experience
        truly remarkable.
      </p>
    </div>
  );
};

export default HomePage;
