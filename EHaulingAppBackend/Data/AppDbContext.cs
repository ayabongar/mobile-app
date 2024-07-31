using Microsoft.EntityFrameworkCore;

public class AppDbContext : DbContext
{
    public DbSet<User> Users { get; set; }
    public DbSet<RideRequest> RideRequests { get; set; }

    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }
}
