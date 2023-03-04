using Xunit;
using kYaSandbox.PingerSpace;
using FluentAssertions;

namespace kYaSandbox.Tests
{
    public class PingerTest
    {
        [Fact]
        public void Pinger_IsPing_True()
        {
            //Arrange.
            //Action.
            var result = Pinger.IsPing("test");
            //Assert.
            result.Should().BeTrue();
        }

        [Fact]
        public void Pinger_IsPing_False()
        {
            //Arrange.
            //Action.
            var result = Pinger.IsPing("");
            //Assert.
            result.Should().BeFalse();
        }
    }
}