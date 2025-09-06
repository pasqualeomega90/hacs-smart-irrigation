class SmartIrrigationCard extends HTMLElement {
  set hass(hass) {
    const zone1 = hass.states['switch.smart_irrigation_zona_1'];
    const zone2 = hass.states['switch.smart_irrigation_zona_2'];
    const sensor1 = hass.states['sensor.smart_irrigation_zona_1'];
    const sensor2 = hass.states['sensor.smart_irrigation_zona_2'];

    this.innerHTML = `
      <ha-card header="Irrigazione Smart MultiZona">
        <div style="display:flex;gap:16px;flex-wrap:wrap;padding:16px">
          <div style="flex:1;min-width:200px;background:#e0f7fa;border-radius:12px;padding:12px;">
            <h3>Zona 1</h3>
            <strong>Stato:</strong> ${zone1 ? zone1.state : 'N/A'}<br>
            <strong>Durata:</strong> ${sensor1 ? sensor1.state + ' min' : 'N/A'}<br>
            <button onclick="hass.callService('switch', 'toggle', { entity_id: 'switch.smart_irrigation_zona_1' })">
              Attiva/Disattiva
            </button>
          </div>
          <div style="flex:1;min-width:200px;background:#f1f8e9;border-radius:12px;padding:12px;">
            <h3>Zona 2</h3>
            <strong>Stato:</strong> ${zone2 ? zone2.state : 'N/A'}<br>
            <strong>Durata:</strong> ${sensor2 ? sensor2.state + ' min' : 'N/A'}<br>
            <button onclick="hass.callService('switch', 'toggle', { entity_id: 'switch.smart_irrigation_zona_2' })">
              Attiva/Disattiva
            </button>
          </div>
        </div>
      </ha-card>
    `;
  }
  setConfig(config) {
    this.config = config;
  }
  getCardSize() {
    return 2;
  }
}
customElements.define('smart-irrigation-card', SmartIrrigationCard);