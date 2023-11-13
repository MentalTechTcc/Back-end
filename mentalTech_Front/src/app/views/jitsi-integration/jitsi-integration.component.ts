import { Component, OnInit, AfterViewInit } from '@angular/core';
import { Router } from '@angular/router';
declare var JitsiMeetExternalAPI: any;
import { ActivatedRoute } from '@angular/router';
import {RelatorioService} from 'src/app/services/relatorio.service';
import {RelatorioSave } from 'src/app/models/Relatorio.models';
import {ConsultaService} from 'src/app/services/consulta.service';
import { switchMap } from 'rxjs/operators';
import {ConsultaRequestId} from 'src/app/models/Consulta.models';

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
  idConsulta: number =0;
 
  isAudioMuted = false;
  isVideoMuted = false;
  mostrarMensagemSucesso = false;
  mostrarMensagemErro = false;


  relatorioPaciente: string = '';

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private relatorioService: RelatorioService,
    private consultaService:ConsultaService,
  ) {
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
     this.tipoConta = params['tipoConta'];
      this.room = params['idAgenda']+'-mentalTech-consulta';
      // coletar a consulta
      this.consultaService.listarPorIdAgenda(params['idAgenda']).subscribe(
        (consulta) => {
          if (consulta) {
            const consultas: ConsultaRequestId[] = Array.isArray(consulta) ? consulta : [consulta];
            if (consultas.length > 0) {
              const primeiraConsulta = consultas[0];
              console.log(primeiraConsulta);
              this.idConsulta = primeiraConsulta.idConsulta;
              // console.log(this.idConsulta);
              // console.log(primeiraConsulta.idConsulta);
            } else {
              console.error('A resposta da API não contém dados de consulta válidos.');
            }
          }
        },
        (error) => {
          console.error('Erro ao obter idConsulta:', error);
        }
      );
      

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
    //console.log("handleClose");
}

handleParticipantLeft = async () => {
    //console.log("handleParticipantLeft", );
    const data = await this.getParticipants();
}

handleParticipantJoined = async () => {
    //console.log("handleParticipantJoined", ); 
    const data = await this.getParticipants();
}

handleVideoConferenceJoined = async () => {
    //console.log("handleVideoConferenceJoined", );
    const data = await this.getParticipants();
}

handleVideoConferenceLeft = () => {
    //console.log("handleVideoConferenceLeft");
    this.router.navigate(['/thank-you']);
}

handleMuteStatus = () => {
    //console.log("handleMuteStatus", ); // { muted: true }
}

handleVideoStatus = () => {
    //console.log("handleVideoStatus", ); // { muted: true }
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
    idConsulta: this.idConsulta,
    dataCadastro: this.formatarDataParaSalvar(new Date())
  };
    //console.log(this.idConsulta)
    this.relatorioService.cadastrarRelatorio(relatorio).subscribe(
      () => this.handleEnvioRelatorioSucesso(),
      error => this.handleEnvioRelatorioErro(error)
    );

}

handleEnvioRelatorioSucesso() {
  console.log('Relatório enviado com sucesso!');
  this.mostrarMensagemSucesso = true;
  console.log(this.mostrarMensagemSucesso )
  this.mostrarMensagemErro = false;

  // Oculta a mensagem
  setTimeout(() => {
    this.mostrarMensagemSucesso = false;
  }, 4000);
}

handleEnvioRelatorioErro(error: any) {
  console.error('Erro ao enviar o relatório:', error);
  this.mostrarMensagemErro = true;
  this.mostrarMensagemSucesso = false;

 
  setTimeout(() => {
    this.mostrarMensagemErro = false;
  }, 4000);
}

  private formatarDataParaSalvar(data: Date): string {
    const yyyy = data.getFullYear();
    const mm = (data.getMonth() + 1).toString().padStart(2, '0');
    const dd = data.getDate().toString().padStart(2, '0');
    return `${yyyy}-${mm}-${dd}`;
  }

  


}