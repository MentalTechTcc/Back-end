import { Component, OnInit, AfterViewInit } from '@angular/core';
import { Router } from '@angular/router';
declare var JitsiMeetExternalAPI: any;
import { ActivatedRoute } from '@angular/router';
import {RelatorioService} from 'src/app/services/relatorio.service';
import { MatSnackBar } from '@angular/material';
import { Relatorio, RelatorioSave } from 'src/app/models/Relatorio.models';

@Component({
    selector: 'app-jitsi',
    templateUrl: './jitsi-integration.component.html',
    styleUrls: ['./jitsi-integration.component.css']
})
export class JitsiComponent implements OnInit, AfterViewInit {

  domain: string = "meet.jit.si";
  room: any;
  options: any;
  api: any;
  user: any;
  tipoConta:any;

 
  isAudioMuted = false;
  isVideoMuted = false;

  relatorioPaciente: string = '';

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private relatorioService: RelatorioService,
    private snackBar: MatSnackBar,
  ) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
     this.tipoConta = params['tipoConta'];
      this.room = params['idAgenda'];
    });

    this.user = {
      name: 'Bianca'
    };
  }

  ngAfterViewInit(): void {
      this.options = {
          roomName: this.room,
          width: 1199,
          height: 680,
          configOverwrite: { prejoinPageEnabled: false },
          interfaceConfigOverwrite: {
              // overwrite interface properties
          },
          parentNode: document.querySelector('#jitsi-iframe'),
          userInfo: {
              displayName: this.user.name
          }
      }

      this.api = new JitsiMeetExternalAPI(this.domain, this.options);

       // Event handlers
      this.api.addEventListeners({
          readyToClose: this.handleClose,
          Left: this.handleParticipantLeft,
          Joined: this.handleParticipantJoined,
          videoConferenceJoined: this.handleVideoConferenceJoined,
          videoConferenceLeft: this.handleVideoConferenceLeft,
          audioMuteStatusChanged: this.handleMuteStatus,
          videoMuteStatusChanged: this.handleVideoStatus
      });
  }

  handleClose = () => {
    console.log("handleClose");
}

handleParticipantLeft = async () => {
    console.log("handleParticipantLeft", );
    const data = await this.getParticipants();
}

handleParticipantJoined = async () => {
    console.log("handleParticipantJoined", ); 
    const data = await this.getParticipants();
}

handleVideoConferenceJoined = async () => {
    console.log("handleVideoConferenceJoined", );
    const data = await this.getParticipants();
}

handleVideoConferenceLeft = () => {
    console.log("handleVideoConferenceLeft");
    this.router.navigate(['/thank-you']);
}

handleMuteStatus = () => {
    console.log("handleMuteStatus", ); // { muted: true }
}

handleVideoStatus = () => {
    console.log("handleVideoStatus", ); // { muted: true }
}

getParticipants() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(this.api.getParticipantsInfo()); // get all s
        }, 500)
    });
}

executeCommand(command: string) {
  this.api.executeCommand(command);;
  if(command == 'hangup') {
      this.router.navigate(['/thank-you']);
      return;
  }

  if(command == 'toggleAudio') {
      this.isAudioMuted = !this.isAudioMuted;
  }

  if(command == 'toggleVideo') {
      this.isVideoMuted = !this.isVideoMuted;
  }
}

enviarRelatorio() {
    const relatorio: RelatorioSave = {
      descricao: this.relatorioPaciente,
      idConsulta: 25,
      dataCadastro: this.formatarDataParaSalvar(new Date())
    };

    this.relatorioService.cadastrarRelatorio(relatorio).subscribe(
      () => this.handleEnvioRelatorioSucesso(),
      error => this.handleEnvioRelatorioErro(error)
    );
  }
  

  private formatarDataParaSalvar(data: Date): string {
    const yyyy = data.getFullYear();
    const mm = (data.getMonth() + 1).toString().padStart(2, '0');
    const dd = data.getDate().toString().padStart(2, '0');
    return `${yyyy}-${mm}-${dd}`;
  }
  
  
  private handleEnvioRelatorioSucesso() {
    this.snackBar.open('Relatório enviado com sucesso!', 'Fechar', {
      duration: 3000,
    });
  }

  private handleEnvioRelatorioErro(error: any) {
    console.error('Erro ao enviar o relatório:', error);
    this.snackBar.open('Erro ao enviar o relatório. Por favor, tente novamente mais tarde.', 'Fechar', {
      duration: 5000,
    });
  }

  


}