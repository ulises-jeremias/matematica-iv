Pendulum p;

void setup() {
        size(640,360);

        // We make a new Pendulum object with
        // an origin location and arm length.
        p = new Pendulum(
          new PVector(width/2, 10),
          125
        );
}

void draw() {
        background(255);
        p.go();
}
