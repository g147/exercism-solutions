class SpaceAge {

    private double sec;
    private static double ear = 31557600;

    SpaceAge(double seconds) {
        sec = seconds;
    }

    double getSeconds() {
        return sec;
    }

    double onEarth() {
        return sec/ear;
    }

    double onMercury() {
        return sec/(0.2408467 * ear);
    }

    double onVenus() {
        return sec/(0.61519726 * ear);
    }

    double onMars() {
        return sec/(1.8808158 * ear);
    }

    double onJupiter() {
        return sec/(11.862615 * ear);
    }

    double onSaturn() {
        return sec/(29.447498 * ear);
    }

    double onUranus() {
        return sec/(84.016846 * ear);
    }

    double onNeptune() {
        return sec/(164.79132 * ear);
    }

}