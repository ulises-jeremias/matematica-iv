class Pendulum {
        PVector location;      // Location of object
        PVector origin;        // Location of arm origin
        float r;               // Length of arm
        float angle;           // Pendulum arm angle
        float aVelocity;       // Angle velocity
        float anAcceleration;  // Angle acceleration
        float damping;         // Arbitrary damping amount

        Pendulum(PVector origin_, float r_) {
                origin = origin_.copy();
                location = new PVector();
                r = r_;
                angle = PI/4;

                aVelocity = 0.0;
                anAcceleration = 0.0;

                // An arbitrary damping so that the Pendulum slows
                // over time
                damping = 0.995;
        }

        void go() {
                update();
                display();
        }

        void update() {
                // It is not necessarily 9.8
                float gravity = 0.4;

                // Formula we worked out for angular acceleration
                anAcceleration = (-1 * gravity / r) * sin(angle);

                // Standard angular motion algorithm
                aVelocity += anAcceleration;
                angle += aVelocity;

                // Apply some damping.
                aVelocity *= damping;
        }

        void display() {
                // Where is the object relative to the origin?
                // Polar to Cartesian coordinates will tell us!
                location.set(r*sin(angle), r*cos(angle), 0);
                location.add(origin);

                stroke(0);

                // The arm
                line(origin.x, origin.y, location.x, location.y);
                fill(175);

                // The object
                ellipse(location.x, location.y, 16, 16);
        }
}
