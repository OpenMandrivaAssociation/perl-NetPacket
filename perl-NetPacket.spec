%define upstream_name    NetPacket
%define upstream_version 1.1.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Assemble and disassemble ethernet packets
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
'NetPacket' provides a base class for a cluster of modules related to
decoding and encoding of network protocols. Each 'NetPacket' descendent
module knows how to encode and decode packets for the network protocol it
implements. Consult the documentation for the module in question for
protocol-specific implementation.

Note that there is no inheritance in the 'NetPacket::' cluster of modules
other than each protocol module being a 'NetPacket'. This was seen to be
too restrictive as imposing inheritance relationships (for example between
the IP, UDP and TCP protocols) would make things like tunneling or other
unusual situations difficult.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.1.1-2mdv2011.0
+ Revision: 657457
- rebuild for updated spec-helper

* Sat Mar 05 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.1.1-1
+ Revision: 642072
- new version

* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-1
+ Revision: 636178
- new version

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.1-1mdv2011.0
+ Revision: 597194
- update to 1.0.1

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.43.1-1mdv2011.0
+ Revision: 552478
- update to 0.43.1

* Fri Mar 26 2010 Jérôme Quelin <jquelin@mandriva.org> 0.42.0-1mdv2010.1
+ Revision: 527744
- update to v0.42.0

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.41.1-2mdv2010.0
+ Revision: 375937
- rebuild

* Thu Apr 02 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.41.1-1mdv2009.1
+ Revision: 363440
- import perl-NetPacket


* Wed Apr 01 2009 cpan2dist 0.41.1-1mdv
- initial mdv release, generated with cpan2dist

