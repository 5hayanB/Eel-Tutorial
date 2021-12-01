function generate() {
    const core = document.getElementById("core").value;
    const bus = document.getElementById("bus_protocol").value;
    const devices = [
        document.getElementById('uart').checked.toString(),
        document.getElementById('spi').checked.toString(),
        document.getElementById('i2c').checked.toString()
    ];
    eel.generate(core, bus, devices);
}
