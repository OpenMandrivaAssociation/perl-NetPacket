%define upstream_name    NetPacket
%define upstream_version v0.42.0

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
