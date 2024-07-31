using Microsoft.AspNetCore.Mvc;
using System.Linq;
using System.Threading.Tasks;
using  userNamespace;


[Route("api/[controller]")]
[ApiController]
public class AuthController : ControllerBase
{
    private readonly AppDbContext _context;

    public AuthController(AppDbContext context)
    {
        _context = context;
    }

    [HttpPost("register")]
    public async Task<IActionResult> Register([FromForm] UserRegisterDto registerDto)
    {
        // Implement registration logic here
        return Ok();
    }

    [HttpPost("login")]
    public async Task<IActionResult> Login([FromForm] UserLoginDto loginDto)
    {
        // Implement login logic here
        return Ok();
    }
}
