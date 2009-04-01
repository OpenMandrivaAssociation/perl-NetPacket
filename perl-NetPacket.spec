
%define realname   NetPacket
%define version    0.41.1
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Assemble and disassemble ethernet packets
Source:     http://www.cpan.org/modules/by-module//%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


