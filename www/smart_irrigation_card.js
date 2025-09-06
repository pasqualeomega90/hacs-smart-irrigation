class SmartIrrigationCard extends HTMLElement {
  set hass(hass) {
    const entity = this.config.entity;
    const state = hass.states[entity];
    this.innerHTML = `
      <ha-card header="Smart Irrigation">
        <div style="padding:16px">
          <strong>Stato:</strong> ${state ? state.state : 'N/A'}<br>
          <button onclick="this.dispatchEvent(new CustomEvent('toggle-irrigation', { bubbles: true }))">
            Attiva/Disattiva
          </button>
        </div>
      </ha-card>
    `;
  }
  setConfig(config) {
    this.config = config;
  }
  getCardSize() {
    return 1;
  }
}
customElements.define('smart-irrigation-card', SmartIrrigationCard);