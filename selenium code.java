package javareply;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import java.util.concurrent.TimeUnit;

public class joker {

	public static void main(String[] args) {
		System.setProperty("webdriver.gecko.driver", "C:\\Users\\Shivi Shrivastava\\Downloads\\geckodriver-v0.20.0-win64\\geckodriver.exe");
        WebDriver driver = new FirefoxDriver();
		driver.get("http://localhost/railway_reservation/mainhome.php");
		WebElement element = driver.findElement(By.id("regu"));
		element.click();
		driver.findElement(By.name("firstname")).sendKeys("Sachin");
		driver.findElement(By.name("lastname")).sendKeys("Tendulkar");
		driver.findElement(By.name("username")).sendKeys("sachin");
		driver.findElement(By.name("password")).sendKeys("1234Sachin@89");
		driver.findElement(By.name("reg_user")).click();

	}

}
