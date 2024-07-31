// User.cs
public class User
{
    public int Id { get; set; }
    public string Username { get; set; }
    public string Password { get; set; }
    public byte[] FaceEncoding { get; set; }
    public string Role { get; set; }
}

// RideRequest.cs
public class RideRequest
{
    public int Id { get; set; }
    public string Username { get; set; }
    public string Destination { get; set; }
    public bool IsDriverAssigned { get; set; }
}
