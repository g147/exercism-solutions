import java.time.LocalDate;
import java.time.LocalDateTime;

class Gigasecond {

    private LocalDateTime current;
    private static long gigaadd = 1000000000L;

    Gigasecond(LocalDate moment) {
        this.current =  moment.atStartOfDay();
    }

    Gigasecond(LocalDateTime moment) {
        this.current = moment;
    }

    LocalDateTime getDateTime() {
        return current.plusSeconds(gigaadd);
    }

}
